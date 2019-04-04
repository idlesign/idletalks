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
