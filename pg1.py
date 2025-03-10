import magenta
import magenta.music as mm
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.protobuf import generator_pb2, music_pb2
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# Load a pre-trained AI model
bundle = magenta.music.read_bundle_file("attention_rnn.mag")
generator = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator(
    model=melody_rnn_sequence_generator.MelodyRnnModel(),
    details="Attention RNN",
    bundle=bundle)

# Create an empty NoteSequence (starting point for melody)
input_sequence = music_pb2.NoteSequence()
input_sequence.tempos.add(qpm=120)  # Set tempo

# Define generation parameters
generator_options = generator_pb2.GeneratorOptions()
generator_options.generate_sections.add(
    start_time=0, end_time=10)  # Generate 10 seconds of music

# Generate the melody
output_sequence = generator.generate(input_sequence, generator_options)

# Save the output as a MIDI file
mm.sequence_proto_to_midi_file(output_sequence, "generated_music.mid")
print("Music generated and saved as 'generated_music.mid'")
# code-alpha
