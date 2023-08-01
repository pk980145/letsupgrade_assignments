var a=10;
var b=-30;

console.log(a+b);

var c='hello';

console.log(c);
console.log(++a);
console.log(a++);
console.log(a);





var obj={first:"hello",
            second:1.2,
            third:3
};

var arr=['q',2,3,4,5,obj];

console.log(arr[5].second);

//alert("wow, you linked your web page to JS")

var username=document.getElementById('user');
function welcome(e){
    // e.preventDefault();
    // var uservalue=username.value;
    // alert("welcome "+uservalue);
    alert("succesful");
}

var form = document.getElementById("form1");

form.addEventListener('submit1',welcome);
alert("hi");