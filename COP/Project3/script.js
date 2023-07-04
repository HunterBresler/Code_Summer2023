//List of questions and results
const Questions = 
[{
    q: "What?",
    a: [{ text: "answer1", res: "fire" },
    { text: "answer2", res: "water" },
    { text: "answer3", res: "earth" },
    { text: "answer4", res: "air" }
    ]
 
},
{
    q: "What?",
    a: [{ text: "answer1", res: "fire" },
    { text: "answer2", res: "water" },
    { text: "answer3", res: "earth" },
    { text: "answer4", res: "air" }
    ]
 
},
{
    q: "What?",
    a: [{ text: "answer1", res: "fire" },
    { text: "answer2", res: "water" },
    { text: "answer3", res: "earth" },
    { text: "answer4", res: "air" }
    ]
 
},
{
    q: "What?",
    a: [{ text: "answer1", res: "fire" },
    { text: "answer2", res: "water" },
    { text: "answer3", res: "earth" },
    { text: "answer4", res: "air" }
    ]
 
},
{
    q: "What?",
    a: [{ text: "answer1", res: "fire" },
    { text: "answer2", res: "water" },
    { text: "answer3", res: "earth" },
    { text: "answer4", res: "air" }
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
            let choicediv = document.createElement("div");
            let choice = document.createElement("input");
            let choiceLabel = document.createElement("label");
            
            choicediv.classList.add("choicediv");

            choice.type = "radio";
            choice.name = "answer"+i;
            choice.value = j;
            choice.id = "answer"+i+j;
    
            choiceLabel.classList.add("choiceLabel");
            choiceLabel.textContent = Questions[i].a[j].text;
            choiceLabel.setAttribute("for", "answer"+i+j);
            
    
            choicediv.appendChild(choice);
            choicediv.appendChild(choiceLabel);
            opt.appendChild(choicediv);
        }
    }
    
}

function gradeQuiz()
{
    let selectedAns;
    let fire, water, earth, air;
    fire = water = earth = air = 0;

    for (let i = 0; i < Questions.length; i++)
    {
        selectedAns = parseInt(document.querySelector('input[name="answer'+i+'"]:checked').value);

        switch (Questions[i].a[selectedAns].res)
        {
            case "fire": 
                fire++;
                break;
            case "water":
                water++;
                break;
            case "earth":
                earth++;
                break;
            case "air":
                air++;
                break;
        }
    }

    let res;
    if (fire > water && fire > earth && fire > air)
    {
        res = "fire"
    }
    else if (air > water && air > earth)
    {
        res = "air"
    }
    else if (water > earth)
    {
        res = "water"
    }
    else
    {
        res = "earth"
    }

    loadRes(res);
}

function loadRes(res)
{
    const totalScore = document.getElementById("res")
    totalScore.textContent = `You're element is ${res}`
}

loadQuestions();

