function percentage_maker () {
	

let portfolio_data = document.getElementsByClassName('portfolio_data')

Array.from(portfolio_data).forEach((element)=>{
	console.log(element)

	let knowledge = element.getElementsByClassName('knowledge')[0]
	let knowledge_width = element.getElementsByClassName('knowledge_width')[0]

	// console.log(knowledge)
	// console.log(knowledge_width)

	let percent = knowledge.querySelectorAll('h1')[1].innerText
	percent = percent.replace('%','%')
	let text = parseInt(percent.replace('%',''))
	// console.log(percent)

	if(text>100){}else{

		knowledge_width.style.width = percent
	}	

})

}

percentage_maker()

let data = document.getElementsByClassName('data')[0]

data.addEventListener('blur',(e) => {
  	// console.log(e)
  	data.innetText = e.target.innerText
});



let percentage_maker_js = document.getElementsByClassName('percentage_maker')

Array.from(percentage_maker_js).forEach((element)=>{
	// console.log(element)
	element.addEventListener('blur',(e) => {
	  	element.innerText = e.target.innerText
	  	console.log(e)
	percentage_maker()
	});

})



let knowledge_known = document.getElementsByClassName('knowledge_known')

Array.from(knowledge_known).forEach((element)=>{
	element.addEventListener('blur',(e) => {
	  		element.innerText = e.target.innerText
	});
})







let work = document.getElementsByClassName('work')[0]

work.addEventListener('blur',(e) => {
  	work.innerText = e.target.innerText
});





let image = document.getElementsByClassName('image')[0]
let portfolio_image = document.getElementsByClassName('portfolio_image')[0]


image.addEventListener('click',(e) => {
  	let image_url = prompt("Enter your portfolio url")

  	if(image_url==' '){}else{
  		portfolio_image.src = image_url
  	}
});






let project__box = document.getElementsByClassName('project__box')

Array.from(project__box).forEach((element)=>{
	element.addEventListener('click',(e) => {
	  	let image_url = prompt("Enter the image url")
		if(image_url!=undefined){
			let image = element.querySelector('img')
			image.src = image_url
		}	


	});
})

let header__text = document.getElementsByClassName('header__text')

