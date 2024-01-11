import random
from config import name_dict

def generate_quiz(num_questions, name_dict, reverse=False):
    quiz = []
    answers = []
    if reverse == True: 
        name_dict_ = dict(zip(name_dict.values(), name_dict.keys()))
    else: 
        name_dict_ = name_dict
    scientific_names = list(name_dict_.keys())
    correct_scientific_names = random.sample(scientific_names, num_questions)

    for correct_scientific_name in correct_scientific_names:
        # correct_scientific_name = random.choice(scientific_names)
        correct_chinese_name = name_dict_[correct_scientific_name]

        # Selecting other four random options
        options = [correct_chinese_name] + random.sample([name_dict_[name] for name in scientific_names if name != correct_scientific_name], 4)
        random.shuffle(options)

        # Append question and options to the quiz
        quiz.append((correct_scientific_name, options))
        answers.append(correct_chinese_name)

    return quiz, answers


def main():
    num_questions = len(name_dict)   # Number of questions in the quiz
    chinese_to_latin = True
    assert num_questions <= len(name_dict)
    quiz, answers = generate_quiz(num_questions, name_dict=name_dict, reverse=chinese_to_latin)
    alphabet = ['A', 'B', 'C', 'D', 'E']
    # Formatting the quiz and answers for display
    quiz_text = "寄生虫学名小测:\n\n"
    for i, (question, options) in enumerate(quiz, 1):
        lang = 'Latin' if chinese_to_latin else 'Chinese'
        quiz_text += f"Question {i}: What is the {lang} name for '{question}'?\n"
        for j, option in enumerate(options, 1):
            quiz_text += f"  {alphabet[j-1]}. {option}\n"
        quiz_text += "\n"

    answer_text = "Answers:\n\n"
    for i, answer in enumerate(answers, 1):
        answer_text += f"Answer {i}: {answer}\n"
    print(quiz_text + answer_text)

if __name__ == '__main__':
    main()