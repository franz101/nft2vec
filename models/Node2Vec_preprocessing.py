import torch
import polars as pl
path = "example_df.parquet"
df = pl.read_parquet(
    path,
    use_pyarrow=True, low_memory=True
    )

dst_col = "f"
src_col = "t"

af = pl.DataFrame(
    df[src_col].unique().append(
    df[dst_col].unique()).unique()
    ).with_column(
    pl.col(src_col).cast(
        pl.Categorical
        ).cat.set_ordering("lexical").alias("val")
 ).with_column(pl.col("val").cast(pl.Int32).alias("val"))[
     [src_col,"val"]
     ]


df = df.lazy().join(af.lazy(),
        on=[src_col]).rename({"val": "src"}).collect()
df = df.lazy().join(
            af.lazy(),
        left_on=dst_col,
        right_on=src_col
        ).rename({"val": "dst"}).collect()

df[["src","dst"]].write_csv("from_to.csv")
af.write_csv("addresses.csv")
af.write_csv("addresses.tsv",has_header=False,sep="\t")