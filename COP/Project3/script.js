//List of questions and results
const Questions = 
[{
    q: "What?",
    a: [{ text: "answer1", res: true },
    { text: "answer2", res: false },
    { text: "answer3", res: true },
    { text: "answer4", res: false }
    ]
 
},
{
    q: "What?",
    a: [{ text: "answer1", res: false },
    { text: "answer2", res: false },
    { text: "answer3", res: false },
    { text: "answer4", res: true }
    ]
 
},
{
    q: "What?",
    a: [{ text: "answer1", res: true },
    { text: "answer2", res: false },
    { text: "answer3", res: false },
    { text: "answer4", res: false }
    ]
 
},
{
    q: "What?",
    a: [{ text: "answer1", res: false },
    { text: "answer2", res: true },
    { text: "answer3", res: false },
    { text: "answer4", res: false }
    ]
 
},
{
    q: "What?",
    a: [{ text: "answer1", res: false },
    { text: "answer2", res: false },
    { text: "answer3", res: false },
    { text: "answer4", res: true }
    ]
 
}]

function loadQuestions() 
{
 
    for (let i = 0; i < Questions.length; i++)
    {
        let question = document.getElementById("question"+i)
        let opt = document.getElementById("opt"+i)

        question.textContent = Questions[i].q;
        opt.innerHTML = ""

        for (let j = 0; j < Questions[i].a.length; j++) 
        {
            const choicesdiv = document.createElement("div");
            const choice = document.createElement("input");
            const choiceLabel = document.createElement("label");
            
            choicesdiv.class = "choicediv";

            choice.type = "radio";
            choice.name = "answer"+i;
            choice.value = j;
    
            choiceLabel.class = "choiceLabel";
            choiceLabel.textContent = Questions[i].a[j].text;
    
            choicesdiv.appendChild(choice);
            choicesdiv.appendChild(choiceLabel);
            opt.appendChild(choicesdiv);
        }
    }
    
}

function gradeQuiz()
{
    let selectedAns = 0;
    let allAnswered = true;

    for (let i = 0; i < Questions.length; i++)
    {
        selectedAns = parseInt(document.querySelector('input[name="answer'+i+'"]:checked').value);
        score = 0;

        if (Questions[i].a[selectedAns].res)
        {
            score++;
        }

        loadScore(score);
    }
}

function loadScore(score)
{
    const totalScore = document.getElementById("score")
    totalScore.textContent = `You scored ${score} out of ${Questions.length}`
}

loadQuestions();

