Reveal.initialize({

    defaultTiming: 120,
    center: true,
    transition: 'slide',
    slideNumber: '',
    progress: true,
    history: true,
    hash: true,

    width: '90%',
    margin: 0,
    minScale: 0.5,
    maxScale: 1.3,

    controls: false,
    controlsTutorial: false,
    mouseWheel: false,
    hideInactiveCursor: true,

    keyboard: {
        37: 'prev', // left arrow
        39: 'next' // right arrow
    },

    dependencies: [
        {
            src: '../static/revealjs/plugin/highlight/highlight.js',
            async: true,
            callback: function () {
                hljs.initHighlightingOnLoad();
            }
        },
        {src: '../static/revealjs/plugin/notes/notes.js', async: true}
    ]
});
