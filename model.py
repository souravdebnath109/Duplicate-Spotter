from speechbrain.pretrained import SpeakerRecognition

# Load the model only once
verification = SpeakerRecognition.from_hparams(
    source="speechbrain/spkrec-ecapa-voxceleb",
    savedir="pretrained_model"
)

def is_speaker_duplicate(file1, file2, threshold=0.75):
    score, prediction = verification.verify_files(file1, file2)
    return (prediction, score)
