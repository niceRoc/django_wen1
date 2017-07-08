/**
 * Created by BretLie on 2017/7/6.
 */

$(function () {

    // 用户名与密码错误信息提示
    var error_name = false;
    var error_pwd = false;

    // 用户名判断
    $('.name_input').blur(function () {
        var sName = $('.name_input').val();

        if (sName.length < 5 || sName.length > 20) {
            $('.user_error').html('请输入5-20个字符的用户名').show();
            error_name = true;
        }
        else {
            $('.user_error').hide();
            error_name = false;
        }
    });

    // 密码判断
    $('.pass_input').blur(function () {
        var sPwd = $('.pass_input').val();

        if(sPwd.length < 8 || sPwd.length > 20) {
            $('.pwd_error').html('密码最少8位，最长20位').show();
            error_pwd = true;
        }
        else {
            $('.pwd_error').hide();
            error_pwd = false;
        }
    });

    $('form').submit(function () {
        $('.name_input').blur();
        $('.pass_input').blur();

        // 只有两个错误信息都为false时才能返回true，才会被表单提交到服务器，交给视图去处理
        return !error_name && !error_pwd
    });

    if ('{{user_error}}' == '1') {
        $('.user_error').html('用户名错误').show();
        error_name = true;
    }
    if ('{{pwd_error}}' == '1') {
        $('.pwd_error').html('密码错误').show();
        error_pwd = true;
    }
});
