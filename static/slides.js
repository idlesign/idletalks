Reveal.initialize({
    controls: true,
    mouseWheel: true,

    progress: true,
    history: true,
    center: true,
    transition: 'slide',
    slideNumber: 'c/t',

    keyboard: {
        37: 'prev', // left arrow
        39: 'next' // right arrow
    },

    dependencies: [
        {
            src: '../static/revealjs/lib/js/classList.js',
            condition: function () {
                return !document.body.classList;
            }
        },
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
