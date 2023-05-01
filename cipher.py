def caesar_cipher(text):
    result = ""
    
    # 이동 거리를 3으로 설정
    shift = 3
    
    for char in text:
        # 알파벳이 아니면 그대로 결과에 추가
        if not char.isalpha():
            result += char
        else:
            # 알파벳이면 이동 거리만큼 이동
            new_char_code = ord(char) + shift
            
            # 알파벳이 대문자 범위를 벗어나면 다시 A부터 시작
            if new_char_code > ord('Z'):
                new_char_code -= 26
            
            # 결과에 새로운 문자 추가
            result += chr(new_char_code)
    
    return result

print(caesar_cipher)
