"use strict";
const { createRoot } = ReactDOM;
const { Breadcrumb, Layout, Menu } = antd;
const { UploadOutlined, DotChartOutlined } = icons;
const { Button, Row, Col, Select, Upload } = antd;
const { Header, Content, Footer } = Layout;
const rowStyle = {};
const App = () => (React.createElement(Layout, { className: "layout" },
    React.createElement(Header, null,
        React.createElement(Menu, { theme: "dark", mode: "horizontal", defaultSelectedKeys: ['NFT2VEC'], items: [{ label: React.createElement("div", null,
                        React.createElement(DotChartOutlined, null),
                        "                 NFT2VEC"), "key": "NFT2VEC" }] })),
    React.createElement(Content, { style: {
            padding: '0 200px',
            //  maxWidth: "50%"
        } },
        React.createElement(Breadcrumb, { style: {
                margin: '16px 0',
            } },
            React.createElement(Breadcrumb.Item, null, "Home"),
            React.createElement(Breadcrumb.Item, null, "Wizard")),
        React.createElement("div", { className: "site-layout-content" },
            React.createElement("h1", null, "Select your data source:"),
            React.createElement(Row, { gutter: [24, 24] },
                React.createElement(Col, { span: 12 }, "Data provider"),
                React.createElement(Col, { span: 12, style: rowStyle },
                    " ",
                    React.createElement(Select, { defaultValue: "Covalent", style: { width: "100%" }, options: [
                            {
                                value: 'Covalent',
                                label: 'Covalent',
                            },
                            {
                                value: 'Dune',
                                label: 'Dune',
                            },
                            {
                                value: 'TheGraph',
                                label: 'TheGraph',
                            },
                            {
                                value: 'BitQuery',
                                label: 'BitQuery',
                            },
                        ] })),
                React.createElement(Col, { span: 12 }, "Dataset"),
                React.createElement(Col, { span: 12 },
                    " ",
                    React.createElement(Select, { defaultValue: "Lens", style: { width: "100%" }, options: [
                            {
                                value: 'Lens',
                                label: 'Lens',
                            },
                            {
                                value: 'ENS',
                                label: 'ENS',
                            },
                            {
                                value: 'ApeCoin',
                                label: 'ApeCoin',
                            },
                        ] })),
                React.createElement(Col, { span: 12 }, " Model"),
                React.createElement(Col, { span: 12 },
                    React.createElement(Select, { defaultValue: "Node2Vec", style: { width: "100%" }, options: [
                            {
                                value: 'Node2Vec',
                                label: 'Node2Vec',
                            },
                            {
                                value: 'TemporalGraph',
                                label: 'TemporalGraph',
                            }
                        ] })),
                React.createElement(Col, { span: 12 }, " Upload Labels"),
                React.createElement(Col, { span: 12 },
                    "    ",
                    React.createElement(Button, { style: { width: "100%" }, icon: React.createElement(UploadOutlined, null) }, "Click to Upload")),
                React.createElement(Col, { span: 24 }, "  "),
                React.createElement(Col, { span: 12 },
                    "  ",
                    React.createElement(Button, { style: { width: "100%" }, href: "https://github.com/franz101/nft2vec/blob/main/dataproviders/dune-python/main.py" }, "Get code")),
                React.createElement(Col, { span: 12 },
                    "  ",
                    React.createElement(Button, { href: "https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/franz101/nft2vec/main/data/lens/v1.json", style: { width: "100%" }, type: "primary" }, "Visualize"))))),
    React.createElement(Footer, { style: {
            textAlign: 'center',
        } }, "2022 ETHSanFrancisco")));
const ComponentDemo = App;
createRoot(mountNode).render(React.createElement(ComponentDemo, null));