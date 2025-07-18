import streamlit as st
from knowledge_graph_builder.workflows.langgraph_router import autonomous_pipeline
from knowledge_graph_builder.utils.graphviz_exporter import export_to_svg
from PIL import Image
import base64

# Page setup
st.set_page_config(page_title="Roadmap.ai", layout="wide")

# Custom CSS Styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

        html, body, div, input, button {
            font-family: 'Poppins', sans-serif;
        }

        html, body {
            background-color: #0f1117;
            color: #ecf0f1;
        }

        .main-title {
            text-align: center;
            font-size: 3.5em;
            font-weight: 700;
            background: linear-gradient(to right, #f12711, #f5af19);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
            animation: fadeIn 1s ease-in-out;
        }

        .subtitle {
            text-align: center;
            font-size: 1.4em;
            color: #bdc3c7;
            margin-bottom: 40px;
        }

        .input-container {
            display: flex;
            justify-content: center;
            margin-bottom: 40px;
        }

        input[type="text"] {
            width: 60%;
            padding: 0.8em;
            border-radius: 12px;
            border: none;
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
            background-color: #1f1f1f;
            color: #fff;
            font-size: 1.1em;
        }

        input[type="text"]:hover, input[type="text"]:focus {
            outline: none;
            box-shadow: 0 0 20px rgba(241, 39, 17, 0.4);
        }

        .svg-container {
            border: 1px solid #2c3e50;
            border-radius: 15px;
            padding: 20px;
            background-color: #1c1c24;
            max-height: 700px;
            overflow-y: auto;
            margin: 20px auto;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
        }

        .download-link {
            text-align: center;
            margin-top: 25px;
            font-size: 1.1em;
        }

        .download-link a {
            background: linear-gradient(90deg, #f12711, #f5af19);
            padding: 10px 20px;
            border-radius: 10px;
            color: white;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .download-link a:hover {
            background: linear-gradient(90deg, #f5af19, #f12711);
        }

        .footer {
            text-align: center;
            font-size: 0.95em;
            color: #95a5a6;
            margin-top: 50px;
        }

        @keyframes fadeIn {
            0% {opacity: 0; transform: translateY(-10px);}
            100% {opacity: 1; transform: translateY(0);}
        }
    </style>
""", unsafe_allow_html=True)

# Header Title with Logo
st.markdown("""
    <div class='main-title'>
        <img src="https://img.icons8.com/fluency/96/brain.png" width="70" style="vertical-align:middle; margin-right: 10px;">
        Roadmap AI
    </div>
""", unsafe_allow_html=True)

# Subtitle
st.markdown("<div class='subtitle'>Generate detailed AI-driven mind maps and learning paths with ease</div>", unsafe_allow_html=True)

# Text input
with st.container():
    st.markdown("<div class='input-container'>", unsafe_allow_html=True)
    topic = st.text_input("🎯 Enter any topic or goal (e.g., 'Roadmap to become an ML Engineer')", "")
    st.markdown("</div>", unsafe_allow_html=True)

# Graph Generation Logic
if topic:
    with st.spinner("🔍 Fetching insights and building your roadmap..."):
        graph = autonomous_pipeline(topic)
        svg_path = export_to_svg(graph)
        st.success("✅ Your knowledge graph is ready!")

        # Render SVG
        with open(svg_path, "r", encoding="utf-8") as f:
            svg_data = f.read()

        b64 = base64.b64encode(svg_data.encode()).decode()

        st.markdown(
            f"""
            <div class="svg-container">
                <object type="image/svg+xml" 
                        data="data:image/svg+xml;base64,{b64}" 
                        style="width:100%; height:600px;">
                    Your browser does not support SVG.
                </object>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Download Button
        with open(svg_path, "rb") as f:
            svg_data = f.read()
            b64 = base64.b64encode(svg_data).decode()
            href = f'<div class="download-link"><a href="data:image/svg+xml;base64,{b64}" download="knowledge_graph.svg">📥 Download as SVG</a></div>'
            st.markdown(href, unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>🚀 Built with ❤️ using <strong>LangGraph</strong>, <strong>Serper</strong>, <strong>Graphviz</strong> & <strong>Streamlit</strong></div>", unsafe_allow_html=True)
