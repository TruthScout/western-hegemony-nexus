import streamlit as st
import yaml
import os

# Set app title
st.set_page_config(page_title="Western Hegemony Dossier", layout="wide")
st.title("🧩 Western Hegemony Dossier: Gaza Case Study")

# Utility function to load YAML
def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

# Base directory for YAML files
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

# Files to load
files = {
    "Key Actors": "actors.yml",
    "Operations": "operations.yml",
    "Financial Influence": "finances.yml",
    "Media & Narrative Control": "narratives.yml",
    "Military & Arms Flow": "military.yml"
}

# Iterate through files and render content
for section_title, filename in files.items():
    st.subheader(f"📌 {section_title}")
    entries = load_yaml(os.path.join(data_dir, filename))

    for entry in entries:
        with st.expander(entry.get("name", "Unnamed Entry")):
            for key, value in entry.items():
                if key == "references" or key == "examples":
                    st.markdown(f"**{key.capitalize()}:**")
                    for ref in value:
                        st.markdown(f"- [{ref}]({ref})")
                elif isinstance(value, list):
                    st.markdown(f"**{key.capitalize()}:** {', '.join(value)}")
                elif key != "name":
                    st.markdown(f"**{key.capitalize()}:** {value}")
    st.markdown("---")
