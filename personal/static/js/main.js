let post = document.getElementsByClassName("project-card");
let horizontal = document.getElementById('horizontal');

// function slideIn(arr) {
//         for (let p of arr) {
//             console.log(arr[0].getBoundingClientRect().left)
//             let rect = p.getBoundingClientRect();
//             if ((window.innerWidth / 2) > rect.left) {
//                 p.classList.add("fadeIn");
//             }
//         }
// }
//
// horizontal.addEventListener('scroll', () => {
//     console.log("Scrolling..");
//     slideIn(post)
// });


function slideOnLoad(el, distance){
        window.addEventListener('load', function(){
            setTimeout(function() {
              console.log("horizontal-loaded")
              el.scroll({
                  left: distance,
                  behavior: 'smooth'
                }
              );
        }, 500);
            setTimeout(function() {
              console.log("horizontal-loaded")
              el.scroll({
                  left: 0,
                  behavior: 'smooth'
                }
              );
        }, 1200);
    })
}


slideOnLoad(horizontal, 500)