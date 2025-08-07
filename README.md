# Dysgraphia Writing Pad

This project provides a **handwriting data collection and visualization tool** to assist in studying dysgraphia. It consists of two main scripts:

1. **Writing Pad** - A fullscreen Tkinter-based application to capture handwriting strokes using mouse or stylus input. It logs precise timestamped pen movements (press, move, release) to a CSV file for further analysis.

2. **Plotting Script** - A Python script that loads the logged handwriting data CSV and visualizes the stroke path on a large graph window, providing a clear visual of the pen motion during writing.

---

## Features

- Fullscreen writing pad window for an immersive writing experience.
- Logs all pen/mouse events with timestamps and coordinates into a CSV file.
- Press `Escape` key to exit the writing pad and save the data properly.
- Separate plotting tool to display handwriting stroke paths from recorded CSV files.
- Large, easy-to-view stroke visualization without any additional overlays or metrics.

---

## Requirements

- Python 3.x
- Tkinter (usually included with standard Python installations)
- pandas
- matplotlib
- numpy

You can install missing packages with:

pip install pandas matplotlib numpy

text

---

## Usage

### 1. Run the Writing Pad

Launch the writing pad application to collect handwriting strokes:

python writing_pad.py

text

- Draw with mouse or stylus on the white canvas.
- All drawing events are recorded to a timestamped CSV file named like `writing_data_<timestamp>.csv`.
- Press `Escape` key or close the window to exit and save data.

### 2. Visualize Stroke Data

After data collection, run the plotting script with your CSV filename to see the handwriting strokes:

python plot_strokes.py

text

Make sure to update the CSV filename inside the plotting script before running.

---

## Notes

- Current setup does not capture pressure data; specialized hardware is needed for pressure sensitivity.
- This project focuses on data collection and visualization; further analysis such as dysgraphia-specific feature extraction can be added.
- For best results, collect data in a quiet environment with a stable input device.

---

## License

This project is provided as-is under the MIT License. Feel free to use and modify it for research and educational purposes.

---

## Contact

For questions or contributions, please contact Deepak M K at deepakmk010@gmail.com.
