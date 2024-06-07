#导入random模块
import random;

#显示游戏规则
print('Rock, Paper, Scissors Game');
print('Rock 打败剪刀');
print('Scissors 打败纸');
print('Paper 打败石头');
print('------------------------------');

#初始化输入列表
input_list = ['rock', 'paper', 'scissors'];

#初始化用户和电脑的对比结果表
result = {
    'rock': {
        'rock': 'draw',
        'paper': 'lose',
        'scissors': 'win'
    },
    'paper': {
        'rock': 'win',
        'paper': 'draw',
        'scissors': 'lose'
    },
    'scissors': {
        'rock': 'lose',
        'paper': 'win',
        'scissors': 'draw'
    }
}

#初始化对比结果的得分表
score = {
    'win': 1,
    'draw': 0,
    'lose': -1
}

#初始化用户得分记录
player_score = 0;

#初始化用户游戏次数
game_count = 0;


#循环直到用户退出
while True:
    #提示用户输入输入列表中可以输入的内容
    print('You can enter: ' + ', '.join(input_list));

    #获取用户输入的内容
    player_move = input();

    #检查用户输入
    if player_move not in input_list:
        print('Invalid move. Please enter ' + ', '.join(input_list));
        continue;

    #输出用户输入的内容
    print('You selected: ' + player_move);

    #随机在Rock, Paper, Scissors中选择一个
    choices = ['rock', 'paper', 'scissors'];
    computer_move = random.choice(choices);

    #输出电脑选择的内容
    print('Computer selected: ' + computer_move);

    #对比用户和电脑的选择结果
    player_result = result[player_move][computer_move];
    player_score = player_score + score[player_result];
    print('You ' + player_result + '!');

    #游戏次数+1
    game_count = game_count + 1;

    #提示用户是否继续
    print('Do you want to play again? (no to quit)');

    #获取用户输入的内容
    play_again = input();

    #如果用户选择不继续，退出循环
    if play_again == 'no':
        break;

    
    #显示分数，获胜次数和游戏轮数
    print('Your play time: ' + str(game_count));
    print('Your score: ' + str(player_score));