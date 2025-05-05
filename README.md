# Phone Number Lookup Automation (Educational Project)

This project helps you automate the process of:

* Generating mobile phone numbers based on a known pattern (e.g., provider, region, ending digits)
* Looking up the name and details associated with a number using the NumLookup API

> **⚠️ Disclaimer**: This project is intended for **educational and ethical** purposes only. Do **not** use this to harass, stalk, or collect data on individuals without consent. Violation of laws and platform terms can have legal consequences. The developer is not responsible for any misuse and following consequences of this sourcecode.

---

## 🚀 Features

* Generate all possible phone numbers using known prefix and suffix digits
* Look up each number using the NumLookup API
* Filter results to find a specific name (e.g., "John Doe")
* API key is safely stored using a `.env` file
* Highly customizable: change name, region, provider, digits, etc.

---

## 📁 Folder Structure

```
PhoneNumberLookup/
├── .env                    # API key file (not tracked by Git)
├── .gitignore             # Hides sensitive and unwanted files
├── README.md              # This file
├── number_generator.py    # Generates phone numbers with specific patterns
└── lookup_script.py       # Checks numbers via API to find the target name
```

---

## 🧰 Prerequisites

1. **Python 3.6+** must be installed.
2. **Git** installed (if you're cloning the repo).
3. A **NumLookup API key**. You can get one from:

   * [https://numlookupapi.com/](https://numlookupapi.com/)

---

## 🔧 Setup Instructions (Step-by-Step)

### 1. Clone the Repository

```bash
git clone https://github.com/sukanyaghosh74/phone-number-lookup.git
cd PhoneNumberLookup
```

### 2. Install Dependencies

Install the required Python libraries:

```bash
pip install requests python-dotenv
```

### 3. Create the `.env` File

Create a file named `.env` in the root directory:

```
NUMLOOKUP_API_KEY=your_real_api_key_here
```

This hides your API key securely from public exposure.

### 4. Set Your Target Info

In both Python scripts, adjust the following variables to your needs:

#### In `number_generator.py`:

```python
provider = "YOUR_DESIRED_PROVIDER"
state = "YOUR_DESIRED_STATE"
known_ending_digits = "XX"
delhi_jio_prefixes = ['XXXXX', 'XXXXX', 'XXXXX']  # Add your real prefixes
```

#### In `lookup_script.py`:

```python
target_name = "YOUR_DESIRED_NAME"
input_file = "generated_numbers.txt"
```

---

## 🧮 How to Run the Project

### Step 1: Generate Numbers

Run the following command to create a list of numbers that match your pattern:

```bash
python number_generator.py
```

This will create a file called `generated_numbers.txt` with numbers like:

```
629101234502
629103567802
...
```

### Step 2: Look Up Each Number

```bash
python lookup_script.py
```

The script will:

* Read each number from the generated list
* Query the NumLookup API for info
* Print info **only if** it matches your `target_name`

---

## 📌 Example Use Case

You know someone uses a Jio number in Delhi, and their number ends in `02`. You suspect their name is "Anurag Sharma".

* Generate all combinations of numbers like `62910xxxxx02`
* Run the lookup to find a number where the name returned is `John Doe`

> ✅ The moment the script finds the name, it stops and shows you the full result.

---

## 🔐 Security Notice

* Always use `.env` to store your API key.
* Never share your `.env` file publicly.
* Respect rate limits and platform rules of the API.

---

## ❓ FAQs

### Q. Can I add more prefixes?

Yes! Add more known prefixes based on your knowledge or data to `prefixes` in `number_generator.py`.

### Q. What if I want to match a different name?

Change the value of `target_name` in `lookup_script.py`.

### Q. Can I use this in another country?

Yes, if you have the proper number format and NumLookup supports that country.

---

## 🧠 Final Thoughts

This project is a great example of combining automation, scripting, and real-world problem-solving. Use it responsibly, improve it further, and share what you’ve learned ethically!

If you liked this project, give it a ⭐ on GitHub!

---

Made with Python, Pandas (Optional), and Curiosity 💻✨
