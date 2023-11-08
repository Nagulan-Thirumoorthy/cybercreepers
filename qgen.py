import re

# Define a function to generate questions from a text
def generate_questions(text):
    # Tokenize the text into sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)
    
    questions = []
    for sentence in sentences:
        # Split each sentence into words
        words = sentence.split()
        
      
        # Generate "What is" questions
        what_question = "What is " + sentence
        questions.append(what_question)


    return questions

# Define the text for which you want to generate questions
text = "Gravity (from Latin gravitas, meaning 'weight'), or gravitation, is a natural phenomenon by which all \
things with mass or energy—including planets, stars, galaxies, and even light—are brought toward (or gravitate toward) \
one another. On Earth, gravity gives weight to physical objects, and the Moon's gravity causes the ocean tides. \\The gravitational attraction of the original gaseous matter present in the Universe caused it to begin coalescing \
and forming stars and caused the stars to group together into galaxies, so gravity is responsible for many of \
the large-scale structures in the Universe. Gravity has an infinite range, although its effects become increasingly \
weaker as objects get further awayScience revolves around studying observations made of the natural world around us,\
and engaging in experimentation. Scientific studies are based on conducting experiments in the real world, and in laboratories.\
Experiments in laboratories are usually conducted under controlled conditions that may not be similar to the real-world conditions.\
Such, experiments, however are useful in understanding phenomena that occur in the real world.\
Scientific experiments can be conducted over and over again, and yield the same results. Scientific studies are,\
therefore, mostly objective and universal. Scientific theories based on findings of experiments are verifiable repeatedly.\
There are different streams of sciences that deal with different areas of study of the world around us.\
For example, while geology deals with the study of the Earth and its formation, in meteorology the study of the \
atmosphere around the Earth and weather patterns is undertaken. On the other hand, astronomy studies the heavenly objects.\
Science deals with the study of the processes and occurrences that we see in the natural world around us.\
Scientific study is undertaken through observation and experiment. It deals with the study of facts that are verifiable.\
When observed facts are studied systematically it becomes a science. A scientific study is made possible through experiments.\
Experiments may be conducted in the real world or in laboratories under controlled conditions. \
A science allows for experiments to be conducted and results to be verified repeatedly. \
There are many different streams of sciences such as physics, chemistry, zoology, botany, geology, meteorology and astronomy."

# Generate questions from the text
generated_questions = generate_questions(text)

# Print the generated questions
for i, question in enumerate(generated_questions):
    print(f"Question {i + 1}:   {question}\n")
