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

        st.sidebar.write('## Filters')
        pfilter = st.sidebar.selectbox(
            'Would you like to apply a filter on the P-Wave?',
            ('No', 'lowpass', 'highpass', 'bandpass')
        )
        if pfilter in ['lowpass', 'highpass']:
            freq = st.sidebar.slider('Cutoff frequency', 1, 10000, 1000)
            stream[0].filter(pfilter, freq=freq, zerophase=True)
            stream[1].filter(pfilter, freq=freq, zerophase=True)
        elif pfilter == 'bandpass':
            freqs = st.sidebar.slider('Cutoff frequency', 1, 10000, (1000, 2000))
            stream[0].filter(pfilter, freqmin=freqs[0], freqmax=freqs[1], zerophase=True)
            stream[1].filter(pfilter, freqmin=freqs[0], freqmax=freqs[1], zerophase=True)
        sfilter = st.sidebar.selectbox(
            'Would you like to apply a filter on the S-Wave?',
            ('No', 'lowpass', 'highpass', 'bandpass')
        )
        if sfilter in ['lowpass', 'highpass']:
            freq = st.sidebar.slider('Cutoff frequency', 1, 2000, 270)
            stream[2].filter(sfilter, freq=freq, zerophase=True)
            stream[3].filter(sfilter, freq=freq, zerophase=True)
            stream[4].filter(sfilter, freq=freq, zerophase=True)
            stream[5].filter(sfilter, freq=freq, zerophase=True)
        elif sfilter == 'bandpass':
            freqs = st.sidebar.slider('Cutoff frequency', 1, 2000, (100, 500))
            stream[2].filter(sfilter, freqmin=freqs[0], freqmax=freqs[1], zerophase=True)
            stream[3].filter(sfilter, freqmin=freqs[0], freqmax=freqs[1], zerophase=True)
            stream[4].filter(sfilter, freqmin=freqs[0], freqmax=freqs[1], zerophase=True)
            stream[5].filter(sfilter, freqmin=freqs[0], freqmax=freqs[1], zerophase=True)

        p_plot, s_plot = plot_traces(stream)

        st.write('## P-Wave')
        st.pyplot(p_plot)

        st.write('## S-Wave')
        st.pyplot(s_plot)

if __name__ == '__main__':
    main()