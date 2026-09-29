export const playAudio=(text, onEnd) =>{
    if(!window.speechSynthesis){
        console.error("Speech synthesis not supported");
        onEnd?.();
        return;
    }
    let utterance = new SpeechSynthesisUtterance(text);
    utterance.lang="en-US";

    utterance.onend = () => {
        onEnd?.();
    };
    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(utterance);
}