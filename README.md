# Job Match AI

A command-line tool that analyzes job postings using the Claude API.
Paste a job description into a text file, and the tool returns:

1. **Fit score** against my personal career criteria (with reasons for each criterion)
2. **Application difficulty** based on required qualifications vs. my strengths
3. **Strengths to highlight** in my resume for that position

## Why I built this

I am a systems engineer with 10 years of experience in business process automation (VBA, RPA).
I built this tool to make my job search more structured, and as my first project using a generative AI API in Python.

## Tech Stack

- Python 3
- Anthropic Claude API
- python-dotenv

## Setup

1. Clone this repository
2. Create a virtual environment and install packages
   ```
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install anthropic python-dotenv
   ```
3. Create a `.env` file and add your API key
   ```
   ANTHROPIC_API_KEY=your-api-key
   ```

## Usage

1. Paste a job description into `job.txt`
2. Run
   ```
   python analyze.py
   ```

## Security

- The API key is stored in `.env` and excluded from Git by `.gitignore`.
- Job descriptions (`job.txt`) are also excluded, as they contain private job search information.

## Design Decisions

- **Separated "fit" from "difficulty"**: In the first version, the AI mixed "does this job match my goals" with "am I qualified." I split them into two separate evaluations so that jobs I want are not scored low just because they are challenging.
- **Explicit scoring rubric**: I defined score ranges in the prompt to keep results consistent. In 4 runs on the same job posting, the total score stayed within a 5-point range (60-65).
