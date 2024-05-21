const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

allSideMenu.forEach(item=> {
	const li = item.parentElement;

	item.addEventListener('click', function () {
		allSideMenu.forEach(i=> {
			i.parentElement.classList.remove('active');
		})
		li.classList.add('active');
	})
});




// TOGGLE SIDEBAR
const menuBar = document.querySelector('#content nav .bx.bx-menu');
const sidebar = document.getElementById('sidebar');

menuBar.addEventListener('click', function () {
	sidebar.classList.toggle('hide');
})


const Lesli=document.querySelectorAll('.box-info li');
const hidden=document.getElementById('switch-hidden');
document.querySelector('.form-input input').addEventListener('input',(e)=>{
	Lesli.forEach((elemnt)=>{
		elemnt.style.display='flex';
	})
	
	Lesli.forEach((element)=>{
		if (!element.querySelector('.text').innerText.toLowerCase().includes(e.target.value.toLowerCase())){
              element.style.display='none';  
		}else{
			element.style.display='flex';
		}
	});
	if(Lesli.length>0){

		if(!Array.from(Lesli).filter((elem)=> elem.checkVisibility()).length){
			hidden.classList.remove('cacher');
		}else{
			hidden.classList.add('cacher');
	    }
	}

})

const NbreCour=document.querySelectorAll('.nbre-cour');
window.addEventListener('resize',()=>{
	if(window.innerWidth < 770) {
		document.getElementById('user').style.display='none'
		sidebar.classList.add('hide');
		NbreCour.forEach((item)=>{
           item.style.display='none';
		})
	}else{
		document.getElementById('user').style.display='initial'
		NbreCour.forEach((item)=>{
			item.style.display='initial';
		 })
	}
})
if(window.innerWidth < 770) {
	document.getElementById('user').style.display='none'
	sidebar.classList.add('hide');
	NbreCour.forEach((item)=>{
	   item.style.display='none';
	})
}else{
	document.getElementById('user').style.display='initial'
	NbreCour.forEach((item)=>{
		item.style.display='initial';
	 })
}



const switchMode = document.getElementById('switch-mode');

switchMode.addEventListener('change', function () {
	console.log('mode');
	if(this.checked) {
		document.body.classList.add('dark');
	} else {
		document.body.classList.remove('dark');
	}
})

