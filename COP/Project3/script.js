//List of questions and results
const Questions = 
[{
    q: "What would you most like to do?",
    a: [{ text: "Go Camping", res: "fire" },
    { text: "Go To The Beach", res: "water" },
    { text: "Go Hiking", res: "earth" },
    { text: "Go ", res: "air" }
    ]
 
},
{
    q: "What?",
    a: [{ text: "answer1", res: "fire" },
    { text: "answer2", res: "earth" },
    { text: "answer3", res: "air" },
    { text: "answer4", res: "water" }
    ]
 
},
{
    q: "What?",
    a: [{ text: "answer1", res: "air" },
    { text: "answer2", res: "water" },
    { text: "answer3", res: "fire" },
    { text: "answer4", res: "earth" }
    ]
 
},
{
    q: "What?",
    a: [{ text: "answer1", res: "air" },
    { text: "answer2", res: "fire" },
    { text: "answer3", res: "earth" },
    { text: "answer4", res: "water" }
    ]
 
},
{
    q: "What?",
    a: [{ text: "answer1", res: "water" },
    { text: "answer2", res: "air" },
    { text: "answer3", res: "fire" },
    { text: "answer4", res: "earth" }
    ]
 
}]

//Loads the questions on the webpage
//For this project I'm just loading them in instantly
function loadQuestions() 
{
    //Loops through every question
    for (let i = 0; i < Questions.length; i++)
    {
        //Get question and answers from Questions array
        let question = document.getElementById("question"+i)
        let opt = document.getElementById("opt"+i)

        question.textContent = Questions[i].q;
        opt.innerHTML = ""

        //Loops through each question's answers
        for (let j = 0; j < Questions[i].a.length; j++) 
        {
            //Create a choice with input and text in a div
            let choicediv = document.createElement("div");
            let choice = document.createElement("input");
            let choiceLabel = document.createElement("label");
            
            //Add class property for CSS
            choicediv.classList.add("choicediv");

            //Add radio properties
            choice.type = "radio";
            choice.name = "answer"+i;
            choice.value = j;
            choice.id = "answer"+i+j;
            
            //Add class for CSS
            //Add text properties/link to button
            choiceLabel.classList.add("choiceLabel");
            choiceLabel.textContent = Questions[i].a[j].text;
            choiceLabel.setAttribute("for", "answer"+i+j);
            
            //Add choice to div and options 
            choicediv.appendChild(choice);
            choicediv.appendChild(choiceLabel);
            opt.appendChild(choicediv);
        }
    }
    
}

//Gets the values from user's selections and assigns the proper result
function gradeQuiz()
{
    //Declare variables
    let selectedAns;
    let fire, water, earth, air;
    fire = water = earth = air = 0;

    //Loop through all selected answers
    for (let i = 0; i < Questions.length; i++)
    {
        //Get selected answers
        selectedAns = parseInt(document.querySelector('input[name="answer'+i+'"]:checked').value);

        //Calculate how many of each answer was choosen
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
            default:
                //something
                break;
        }
    }

    let res;

    //Calculate result of quiz
    if (fire > water && fire > earth && fire > air)
    {
        res = "fire";
    }
    else if (air > water && air > earth)
    {
        res = "air";
    }
    else if (water > earth)
    {
        res = "water";
    }
    else
    {
        res = "earth";
    }

    loadRes(res);
}

//Displays results beneath quiz
//Could load new webpage, but I'm not doing all that
function loadRes(res)
{
    const result = document.getElementById("res");
    result.textContent = `You're element is ${res}`;
}

loadQuestions();

