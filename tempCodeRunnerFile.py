cv2.putText(frame, 'Current: ' + current_word, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # for idx, word in enumerate(words_history):
    #     cv2.putText(frame, f'Hist{idx+1}: {word}', (50, 100 + idx * 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)