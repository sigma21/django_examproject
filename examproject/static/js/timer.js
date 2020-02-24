
// Set the date we're counting down to
const start = document.getElementById("start-time").innerHTML;
const countDownDate = Number(start) + 40*60*1000;
const finish = document.getElementById("finish-time").innerHTML=countDownDate;


// Update the count down every 1 second
const x = setInterval(function() {

  // Get today's date and time
  const now = new Date().getTime();
  // Find the distance between now and the count down date
  let distance = countDownDate*1000 - now;

  // Time calculations for days, hours, minutes and seconds
  // const days = Math.floor(distance / (1000 * 60 * 60 * 24));
  // const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
  // Output the result in an element with id="timer"
  document.getElementById("timer").innerHTML = minutes + "m " + seconds + "s ";

    
  // If the count down is over, write some text 
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("timer").innerHTML = "EXPIRED";
  }
}, 1000);
