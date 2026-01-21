# Processing and visualizing data from high-performance liquid chromatography

The [original dataset](https://search.nfdi4chem.de/dataset/10-14272-wgjybqwdbmlolo-lgmdplhjsa-n-chmo0000796) results from high-performance liquid chromatography coupled with mass spectrometry (HPLC-MS), which is a technique used to separate and identify components in a chemical sample. Specifically, the associated organic molecule is C₂₀H₁₆BF₂NO₃S. 


This dataset contains:
- Spectrum file, which contains a single spectrum over a retention-time, and some background information about instrument type, polarity, and base peak;
- ASCII file, which includes many individual MS scans, each contains scan time, polarity, ionization mode, m/z range, and a list of m/z-intensity pairs;
- DX file, which includes metadata and multiple time pages.


This project:
- First, converts .spectrum, .ascii, and .dx data file into tables in .csv format.
- Then, visualize the data for easier interpretation. 
