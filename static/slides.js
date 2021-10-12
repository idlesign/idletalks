Reveal.initialize({

    defaultTiming: 120,
    center: true,
    transition: 'slide',
    slideNumber: 'c/t',
    progress: true,
    history: true,
    hash: true,

    width: '70%',
    margin: 0,
    minScale: 0.5,
    maxScale: 1.3,

    controls: true,
    controlsTutorial: false,
    mouseWheel: true,
    hideInactiveCursor: true,

    keyboard: {
        37: 'prev', // left arrow
        39: 'next' // right arrow
    },

    plugins: [ RevealHighlight, RevealNotes ]
});
