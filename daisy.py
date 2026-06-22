import datetime
import random
import time

count = 0

jokes = [
    "i told my code there was a problem with it.\nit said 'no, the problem is YOU' and refused to run.",
    "spent 3 hours fixing a bug today.\nturned out i forgot a colon. classic.",
    "my code worked first try once.\nstill not sure what i did wrong.",
    "debugging is basically being a detective in a crime movie\nwhere you are also the murderer.",
    "asked DAISY to tell a joke.\nshe pointed at my code instead.",
]


motivations = [
    "every bug you fix is a skill you keep forever.",
    "you dont have to be perfect, just show up and try again tomorrow.",
    "a finished project beats a perfect one that never got submitted.",
    "building this from scratch already counts as real progress.",
    "ai is not magic, its just logic and patience. you have both.",
    "the days you want to quit are usually the ones that teach you the most.",
]

tips = [
    "Pomodoro: study 25 min then break 5 min. repeat 4 times.",
    "Active Recall: after reading, close the book and recall from memory.",
    "Teach to Learn: explain what you studied out loud. if you can teach it you know it.",
    "Code Every Day: even 20 minutes daily beats 5 hours once a week.",
    "Build Projects: books teach theory, projects teach reality.",
    "Spaced Repetition: review topics after 1 day, 3 days, then 7 days.",
]

quiz_data = [
    ("What does AI stand for?", "artificial intelligence"),
    ("Which language is most used for AI?", "python"),
    ("What is ML short for?", "machine learning"),
    ("Who created ChatGPT?", "openai"),
    ("What does NLP stand for?", "natural language processing"),
    ("What type of chatbot is DAISY?", "rule based"),
    ("Name one Python AI library.", ["numpy", "pandas", "tensorflow", "pytorch", "scikit"]),
]

roadmap = {
    "1": [
        "1. Learn Python basics - variables, loops, functions, conditions",
        "2. Practice small projects - calculator, to-do list, chatbot",
        "3. Learn NumPy and Pandas for data handling",
        "4. Study basic stats - mean, median, probability",
        "5. Try Machine Learning with Scikit-learn",
        "6. Build one project and put it on GitHub",
    ],
    "2": [
        "1. Master ML algorithms - regression, decision trees, KNN, SVM",
        "2. Learn data visualization with Matplotlib and Seaborn",
        "3. Practice on real datasets from Kaggle",
        "4. Start Deep Learning with TensorFlow or PyTorch",
        "5. Learn NLP basics - tokenization, sentiment analysis",
        "6. Build a portfolio project with proper documentation",
    ],
    "3": [
        "1. Deep dive into CNNs, RNNs and Transformers",
        "2. Study MLOps - how to deploy and monitor models",
        "3. Read foundational papers like Attention Is All You Need",
        "4. Contribute to open source AI projects on GitHub",
        "5. Pick a specialization - Computer Vision, NLP, or RL",
        "6. Deploy a real AI product as an API or web app",
    ],
}

def thinking():
    print("DAISY : thinking...", end="\r")
    time.sleep(1)
    print(" " * 30, end="\r")

def startup():
    print()
    print("  Hi, I am DAISY.")
    print("  Type 'who are you' to know more about me, or 'what can you do' to see what I can do.")
    print()


def get_reply(msg):
    msg = msg.lower().strip()

    if msg in ["hi", "hello", "hey", "hii"]:
        return "Hello! I am DAISY. How can I help you today?"
    elif "good morning" in msg: return "Good Morning! New day, new chance to learn something."
    elif "good night"   in msg: return "Good Night! Rest well. Fresh mind learns faster."
    elif "good evening" in msg: return "Good Evening! How did the day go?"

    elif "happy"   in msg: return "Great to hear. Keep that energy going!"
    elif "sad"     in msg or "upset"   in msg: return "Tough days happen. Take a break and come back stronger."
    elif "bored"   in msg: return "Try typing quiz or roadmap. something productive!"
    elif "tired"   in msg: return "Rest is part of the process. take a break."
    elif "stress"  in msg or "worried" in msg: return "One task at a time. you got this."

    elif msg in ["joke", "tell me a joke"]:                  return "THINK:" + random.choice(jokes)
    elif msg in ["motivate me", "motivation", "inspire me"]: return "THINK:" + random.choice(motivations)
    elif msg in ["study tip", "tip", "study tips"]:          return "THINK:" + random.choice(tips)
    elif msg in ["quiz", "test me"]:                         return "QUIZ"
    elif msg in ["roadmap", "how to learn ai"]:              return "ROADMAP"

    elif msg in ["time", "what time is it"]:
        return "Time: " + datetime.datetime.now().strftime("%I:%M %p")
    elif msg in ["date", "today", "what day is today"]:
        return "Date: " + datetime.datetime.now().strftime("%A, %d %B %Y")

    elif msg in ["what is ai", "ai"]:
        return "THINK:AI = Artificial Intelligence. teaching machines to think and make decisions like humans."
    elif msg in ["what is ml", "ml", "machine learning"]:
        return "THINK:ML = Machine Learning. machines learn from data on their own without fixed rules."
    elif msg in ["what is python", "python"]:
        return "THINK:Python is the top language for AI. simple syntax and powerful libraries like NumPy and TensorFlow."

    elif msg in ["count", "message count"]:
        return f"We have exchanged {count} messages this session."
    elif msg in ["about", "who are you", "who made you", "your creator"]:
        return "I am DAISY - Disha's AI Smart and Intelligent System. Disha built me from scratch. I'm a rule-based AI, so I follow predefined rules to chat with you."
    elif msg in ["thanks", "thank you", "ty"]: return "You are welcome!"
    elif msg in ["bye", "exit", "quit"]:       return "EXIT"

    elif msg in ["help", "commands","what can you do","features"]:
        return (
            "Here's what I can assist you with:\n\n"
            "  hi / hello                  -> Start a conversation\n"
            "  good morning/night/evening  -> Greetings & wishes\n"
            "  happy / sad / bored /\n"
            "  tired / stress              -> Emotional support\n"
            "  joke                        -> Random joke\n"
            "  motivate me                 -> Motivational quote\n"
            "  study tip                   -> Learning advice\n"
            "  quiz                        -> AI quiz\n"
            "  roadmap                     -> AI learning path\n"
            "  time / date                 -> Current time or date\n"
            "  what is ai/ml/python        -> Quick explanations\n"
            "  count                       -> Message count\n"
            "  about                       -> Learn about DAISY\n"
            "  thanks                      -> Acknowledge response\n"
            "  bye                         -> End session"
        )
    else:
        return "I didn't get that. Try asking me 'what I can do', or type 'help' for available options."

def run_quiz():
    thinking()
    print("DAISY : Starting AI Quiz. answer in your own words.\n")
    
    score = 0
    questions = random.sample(quiz_data, 5)

    for i in range(5):
        question = questions[i][0]
        answer = questions[i][1]

        user_ans = input(f"  Q{i+1}: {question}\n  You: ").lower().strip()
        thinking()

        # check if answer is correct
        if isinstance(answer, list):
            is_correct = False
            for a in answer:
                if a in user_ans:
                    is_correct = True
                    break
        else:
            is_correct = answer in user_ans

        if is_correct:
            print("  Correct!\n")
            score += 1
        else:
            if isinstance(answer, list):
                correct_answer = answer[0]
            else:
                correct_answer = answer
            print(f"  Answer was: {correct_answer}\n")

    print(f"  Your Score: {score}/5")

    if score == 5:
        print("  Perfect!\n")
    elif score >= 3:
        print("  Good effort!\n")
    else:
        print("  Keep studying!\n")

def show_roadmap():
    thinking()
    print("DAISY : AI Learning Roadmap")
    print("  Select level:  1 = Beginner   2 = Intermediate   3 = Advanced\n")
    choice = input("  Your level: ").strip()
    steps = roadmap.get(choice)
    thinking()
    if steps:
        print()
        for s in steps:
            print("  " + s)
    else:
        print("  Please enter 1, 2 or 3.")
    print()


def main():
    global count
    startup()

    while True:
        try:
            user_input = input("You   : ")
        except KeyboardInterrupt:
            print("\nDAISY : Goodbye!")
            break

        if not user_input.strip():
            print("DAISY : say something!\n")
            continue

        count += 1
        reply = get_reply(user_input)

        if reply == "EXIT":
            thinking()
            now = datetime.datetime.now()
            print()
            print(f"  Session ended at {now.strftime('%I:%M %p')} on {now.strftime('%d %b %Y')}.")
            print()
            print("  It was great talking with you today.")
            print(f"  We exchanged {count} messages this session.")
            print()
            print("  Come back anytime. DAISY will be right here.")
            print()
            break
        elif reply == "QUIZ":
            run_quiz()
        elif reply == "ROADMAP":
            show_roadmap()
        elif reply.startswith("THINK:"):
            thinking()
            print("DAISY : " + reply[6:] + "\n")
        else:
            print("DAISY : " + reply + "\n")


if __name__ == "__main__":
    main()
