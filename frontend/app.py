import requests
import streamlit as st


st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide"
)


BACKEND_URL = "http://127.0.0.1:8000"


st.title("⚖️ LegalEase")
st.subheader("AI-Powered Legal Document Generator")

st.write(
    "Create professional legal document drafts using LegalEase."
)

st.divider()


document_type = st.selectbox(
    "Document Type",
    [
        "Non-Disclosure Agreement",
        "Employment Contract",
        "Residential Lease Agreement"
    ]
)


parties = st.text_area(
    "Parties",
    placeholder="Example: Company: ABC Technologies Pvt Ltd; Employee: John Doe"
)


terms = st.text_area(
    "Terms and Conditions",
    placeholder="Example: Confidentiality; Payment terms; Agreement duration"
)


effective_date = st.text_input(
    "Effective Date",
    placeholder="Example: 26 September 2026"
)


if st.button("Generate Document", type="primary"):

    if not parties.strip():
        st.error("Please enter the parties.")

    elif not terms.strip():
        st.error("Please enter the terms and conditions.")

    else:

        request_data = {
            "document_type": document_type,
            "parties": parties,
            "terms": terms,
            "effective_date": effective_date
        }

        try:

            response = requests.post(
                f"{BACKEND_URL}/generate",
                json=request_data,
                timeout=120
            )

            if response.status_code == 200:

                result = response.json()

                st.success("Document generated successfully!")

                st.subheader("Generated Document")

                edited_document = st.text_area(
                    "Preview / Edit Document",
                    value=result["content"],
                    height=500
                )

                st.download_button(
                    label="Download TXT",
                    data=edited_document,
                    file_name="LegalEase_Document.txt",
                    mime="text/plain"
                )

                st.info(
                    f"Generation mode: {result.get('mode', 'unknown')}"
                )

            else:

                st.error(
                    f"Backend error: {response.status_code}"
                )

                st.code(response.text)

        except requests.exceptions.RequestException as exc:

            st.error(
                "Could not connect to the LegalEase backend."
            )

            st.code(str(exc))


st.divider()

st.caption(
    "LegalEase generates AI-assisted legal document drafts. "
    "Documents should be reviewed by a qualified legal professional "
    "before use."
)