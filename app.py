import streamlit as st
import matplotlib.pyplot as plt
import obspy
plt.rcParams['lines.linewidth'] = 1

def parse_seg_file(file):
    return obspy.read(file)

def plot_traces(stream: obspy.Stream):
    p_fig, p_axs = plt.subplots(2, 1)
    s_fig, s_axs = plt.subplots(2, 1)

    p_axs[0].plot(stream[0].data)
    p_axs[1].plot(stream[1].data)

    s_axs[0].plot(stream[2].data)
    s_axs[0].plot(stream[4].data)
 
    s_axs[1].plot(stream[3].data)
    s_axs[1].plot(stream[5].data)

    return p_fig, s_fig

def main():
    st.title('SEG2 Reader')

    file = st.file_uploader('Upload SEG2 file')

    if file is not None:
        stream = parse_seg_file(file)
        p_plot, s_plot = plot_traces(stream)

        st.pyplot(p_plot)
        st.pyplot(s_plot)

if __name__ == '__main__':
    main()