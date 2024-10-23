# Task 6: Create a feature to translate the audio into Hindi . The system will listen the english audio from user and it will convert into Hindi word. If the system does not understand the audio it will ask repeat one more time to make it better.. The audio should be in English word only . This translation feature work on only after 6 PM IST timing and before that it should show message like please try after 6 PM IST as well as it should not translate any english which is start with M and O apart from that it should translate all other words .


## Overview
This task translates spoken English audio to Hindi, operational only after 6 PM IST. Additionally, words starting with 'M' or 'O' are excluded from translation.

## Model
- The model uses speech recognition to capture audio and translate it.
- Time and character constraints are implemented.

## Data
- Data consists of English-Hindi translation pairs.
- Sentences are preprocessed and tokenized.

## Files
- `task6.ipynb`: Contains the audio translation model.
- `gui.py`: GUI script to interact with the model.

## Setup
1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd <repo_name>

