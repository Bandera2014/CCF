const page = window.open("index.html")


const automotive = [1, 434, 42, 131, 5, 3, 13, 21, 2421, 5, 231, 3]
const construction = [3]
const foyer = ["Hopf Equipment"]
const assembly = [69]
// makes list of loctaions


// function toList(listy, name,id) {
//   let all = document.getElementById(id)
//   let div = document.createElement("div")
//   div.innerHTML = name
//   div.classList.add("ddm")
//   all.appendChild(div)
//   for (var i in listy) {
//     listy[i] = new b(listy[i])
//     all.appendChild(listy[i].button)
//   }
// }
var butten=[]
function toList(listy, name) {
  let all = document.createElement("div")
  let div = document.createElement("div")
  div.innerHTML = name
  div.classList.add("ddm")
  all.appendChild(div)
  for (var i in listy) {
    listy[i] = new b(listy[i])
    all.appendChild(listy[i].button)
  }
  butten.push(all)
}



class b {
  constructor(name) {
    this.button = document.createElement("a")
    this.button.innerHTML = name+"<br>"
    this.button.style=""
    this.button.href = ("index.html?search="+name)
    this.button.addEventListener("click", function () {
      
    });
    
  }
}

toList(automotive, "Automotive")
toList(foyer, "Foyer")
toList(assembly, "Assembly")
toList(construction, "Construction")


// Original: 
// https://stackoverflow.com/questions/39253980/how-to-draw-a-point-on-image-based-on-coordinate-value-of-various-points-on-imag
var canvas = document.getElementById('imgcanvas');
var context = canvas.getContext("2d");

var mapSprite = new Image();
mapSprite.src = "https://mcamp117.github.io/NavTest/HTML/drawMaps/MASTER%20SICTC%20FLOOR%20PLAN.jpg";
var Button = function () {
    this.Sprite = new Image();
    this.Sprite.src = "/images/dropdown.png"
    this.Width = 75;
    this.Height = 75;
    this.XPos = 0;
    this.YPos = 0; 
}

var buttons = []

canvas.addEventListener("mousemove", mouseClicked, false);

var addButton = function (cord1,cord2) {

    var button = new Button();
    button.XPos = cord1 - (button.Width / 2);
    button.YPos = cord2 - button.Height;

    buttons.push(button);
}

function mouseClicked(event) {
  for (var i = 0; i < buttons.length; i++) {
    //https://stackoverflow.com/questions/55677/how-do-i-get-the-coordinates-of-a-mouse-click-on-a-canvas-element
    var rect = canvas.getBoundingClientRect()
    var currentMousePos = [event["clientX"]- rect.left-37.5,event["clientY"]- rect.top-35]
    var currentButtonPos = [buttons[i]["XPos"],buttons[i]["YPos"]]
    if (currentButtonPos[0]-25 < currentMousePos[0] && currentButtonPos[0]+25 > currentMousePos[0] && currentButtonPos[1]-25 < currentMousePos[1] && currentButtonPos[1]+25 > currentMousePos[1]) {
      document.getElementById("main").style.display = "block"
      document.getElementById("main").innerHTML=butten[i].innerHTML
    }
  }
}

var draw = function () {
    context.fillStyle = "#000";
    context.fillRect(0, 0, canvas.width, canvas.height);

    context.drawImage(mapSprite, 0, 0, 700, 700);

    for (var i = 0; i < buttons.length; i++) {
        var tempMarker = buttons[i];
        context.drawImage(tempMarker.Sprite, tempMarker.XPos, tempMarker.YPos, tempMarker.Width, tempMarker.Height);
    }
};

addButton(530,180)

addButton(360,210)
addButton(300,150)

addButton(100,450)


setInterval(() => {draw()}, 1000);