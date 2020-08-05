
var user1 = {
    name: 'Вася',
    age: 23,
    adress: 'Чебоксары'
};

var user2 = {
    name: 'Маша',
    age: 19,
    adress: 'Белгород'
};


function user_add_bonus(user, bonus_count) {
    user.bouns_count += bonus_count;
    user.bonus_level = Math.floor(user.bouns_count / 10000);
    if (user.bonus_level > 3) {
        user.bonus_level = 3;
    }
    console.log('Бонусный уровень покупателя ', user.name, ' : ', user.bonus_level)
}
