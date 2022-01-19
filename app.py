from io import BytesIO
import streamlit as st
import numpy as np
from obspy import read as seg2read

def parse_seg_file(file):
    return seg2read(file)

def main():
    st.title('SEG2 Reader')

    file = st.file_uploader('Upload SEG2 file')

    if file is not None:
        stream = parse_seg_file(file)
        for trace in stream:
            st.line_chart(data=trace.data)

if __name__ == '__main__':
    main()