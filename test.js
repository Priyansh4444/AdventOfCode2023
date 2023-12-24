// function foo(y, condition) {
//     if (condition) {
//       console.log(x);
//       console.log(x);
//     }
//     var x = 3;
//   }
  
// foo(1, true);
  
// console.log();
// t = {}
// if (0){
//   console.log("yo");
// }
// try {
//   throw {
//     toString() {
//       return "I'm an object!";
//     },
//   };
// } catch (e) {
//   console.log(e.toString()); // Logs: "I'm an object!"
// }

function getMonthName(mo) {
  mo--; // Adjust month number for array index (so that 0 = Jan, 11 = Dec)
  const months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
  ];
  if (months[mo]) {
    return months[mo];
  } else {
    throw new Error("InvalidMonthNo"); // throw keyword is used here
  }
}
function logMyErrors(error) {
  console.log('Error: ', error);
}
try {
// statements to try
  monthName = getMonthName(myMonth); // function could throw exception
} catch (e) {

  monthName = "unknown";
  logMyErrors(e); // pass exception object to error handler (i.e. your own function)
}
try {
  try {
    throw new Error("oops");
  } catch (ex) {
    console.error("inner", ex.message);
    throw ex;
  } finally {
    console.log("finally");
    return;
  }
} catch (ex) {
  console.error("outer", ex.message);
}
finally {
  console.log("poorp")
}