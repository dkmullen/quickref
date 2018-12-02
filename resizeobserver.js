const r = new ResizeObserver(n => {
    console.log('resize', document.getElementById('box4').clientWidth)
})

r.observe(document.getElementById('box4'))
