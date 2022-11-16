#/usr/bin/env python
# -*- coding: utf-8 -*-


def write_list(file, list):
    file.write('[')
    for i in range(len(list)):
        file.write(str(list[i]))
        file.write(' ')
    file.write(']\n')
    
    return file


def write_yaku(file, yaku_list):    
    
    return file


def write_log_init(file, field_cards, yamafuda, my_cards, your_cards, my_getcards, your_getcards, my_score, your_score, my_total_score, your_total_score, my_koikoi, your_koikoi):
    file.write('field_cards\n')
    file = write_list(file, field_cards)
    
    file.write('yamafuda\n')
    file = write_list(file, yamafuda)
    
    file.write('my_cards\n')
    file = write_list(file, my_cards)
    
    file.write('your_cards\n')
    file = write_list(file, your_cards)
    
    file.write('my_getcards\n')
    file = write_list(file, my_getcards)
    
    file.write('your_getcards\n')
    file = write_list(file, your_getcards)
    
    file.write('my_score\n')
    file.write(str(my_score) + '\n')
    
    file.write('your_score\n')
    file.write(str(your_score) + '\n')
    
    file.write('my_total_score\n')
    file.write(str(my_total_score) + '\n')
    
    file.write('your_total_score\n')
    file.write(str(your_total_score) + '\n')
    
    file.write('my_koikoi_flag\n')
    file.write(str(my_koikoi) + '\n')
    
    file.write('your_koikoi_flag\n')
    file.write(str(your_koikoi) + '\n')
    
    return file


def write_log(file, month, index, field_cards, yamafuda, my_cards, your_cards, my_getcards, your_getcards, my_score, your_score, my_total_score, your_total_score, my_koikoi, your_koikoi):
    file.write('month\n')
    file.write(str(month+1) + '\n')
    
    file.write('tern\n')
    file.write(str(index+1) + '\n')
    
    file = write_log_init(file, field_cards, yamafuda, my_cards, your_cards, my_getcards, your_getcards, my_score, your_score, my_total_score, your_total_score, my_koikoi, your_koikoi)
    
    return file


def write_result_month(file, month, field_cards, yamafuda, my_cards, your_cards, my_getcards, your_getcards, my_score, your_score, my_total_score, your_total_score, my_koikoi, your_koikoi):
    file.write('month\n')
    file.write(str(month+1) + '\n')
    
    
    file = write_log_init(file, field_cards, yamafuda, my_cards, your_cards, my_getcards, your_getcards, my_score, your_score, my_total_score, your_total_score, my_koikoi, your_koikoi)
    
    return file


def write_result_game(file, field_cards, yamafuda, my_cards, your_cards, my_getcards, your_getcards, my_score, your_score, my_total_score, your_total_score, my_koikoi, your_koikoi):
    
    file = write_log_init(file, field_cards, yamafuda, my_cards, your_cards, my_getcards, your_getcards, my_score, your_score, my_total_score, your_total_score, my_koikoi, your_koikoi)
    
    return file