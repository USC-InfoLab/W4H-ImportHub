# W4H ImportHub: Effortlessly Bridging Your Data to the W4H Ecosystem

W4H ImportHub is your gateway to seamlessly merging your stored datasets (e.g., CSV files) with the expansive world of our innovative W4H platform. Crafted with a user-centric interface, this hub goes beyond mere data import; it intelligently foresees your mapping requirements, weaving the nuanced threads of your datasets into the fabric of the W4H ecosystem with grace and precision. Experience not just an import, but a harmonious fusion of data realms by linking your data world to our expanding W4H platform.

## Table of Contents

- [Documentation](#documentation)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Documentation

Dive deep into the heart of W4H ImportHub and understand its nuances by visiting the [W4H ImportHub Documentation](www.google.com).


## Features

- **One-Click W4H Database Instance Creation:** Dive into the world of W4H with unparalleled ease. With just a simple click, W4H ImportHub unfurls a complete W4H instance in your database. Give it a name, click, and watch the magic unfold.

- **Drag, Drop, & Integrate CSV Effortlessly:** Streamline your data migration journey with our effortless CSV integration. Drag and drop your file, harness our intuitive mapping suggestions, or curate your own – and swiftly funnel your data into the W4H platform.

- **Intuitive Mapping Dashboard:** Our interface doesn't just allow you to define mappings between your data columns and W4H tables; it thinks alongside you, suggesting mappings grounded in intelligent recognition patterns.

- **Configurable DNA:** W4H ImportHub is crafted with a flexible DNA. Tailor it, tweak its settings, define what tables to involve, and let it resonate with your specific W4H blueprint. Especially robust for those navigating the waters of time-series data, this feature ensures you wield a tool attuned to your every need.


## Prerequisites

Before you embark on your journey with W4H ImportHub, please ensure:

- Python 3.x is your trusted companion.
- Essential dependencies are in your toolkit (Check the [Installation](#installation)).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/USC-InfoLab/W4H-ImportHub.git
   ```

2. Install the required dependencies:

    ```bash
    cd W4H-ImportHub
    pip install -r requirements.txt
    ```

## Usage

1. **Setup Configuration:** Before diving into the import process, ensure your environment is set up correctly (see [Installation](#installation)). Copy the `config.yaml.example` to `config.yaml`. Within this configuration file, input your database connection details. You can either leverage our default recommended platform configuration or customize it to better match your specific requirements.

2. **Launch the Streamlit app:** Run the W4H ImportHub Streamlit dashboard:
```bash
streamlit run import_hub_main.py
```
This will provide an address which you can use to access the UI in your web browser.

3. **Database Instance Decision:** Once on the UI, you'll have the option to either populate an existing W4H database instance or initiate a new one.

4. **CSV Integration:** Upload the CSV file you intend to incorporate into the W4H platform.

5. **Mapping Configuration:** After finishing the upload, the tool will intelligently suggest a default mapping grounded in the similarity between the CSV column names and the W4H table names. At this stage, review and, if needed, adjust the mapping using the intuitive UI dashboard.

6. **Populate the W4H Database:** With the mapping set, confirm the import process. The tool will then swing into action, meticulously populating the W4H database according to your directives.

By following these steps, you can easily bridge the gap between your offline datasets and the expansive world of the W4H platform.


## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](https://github.com/USC-InfoLab/W4H-ImportHub/blob/main/LICENSE). Please keep in mind while the code can be modified and used freely, it's essential to acknowledge or credit the original project if used or referenced in a public domain or another project.
