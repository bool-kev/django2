
Array.from(document.querySelectorAll('p>label')).map((e)=>{
    e.classList.add('form-label')
});
Array.from(document.querySelectorAll('form>p')).map((e)=>{
    e.classList.add('form-group')
});
Array.from(document.querySelectorAll('form>p>input:not([type="checkbox"],[type="radio"],[type="submit"]),form>p>select,form>p>textarea')).map((e)=>{
    e.classList.add('form-control')
});

Array.from(document.querySelectorAll(".errorlist li")).map((e)=>{
    e.style.color='red'
    e.textContent+='👇'
})


