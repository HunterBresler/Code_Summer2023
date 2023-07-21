function isStrongPassword(password){
    if (password.length < 8){
        return false;
    }
    else if (password.search("password") != -1){
        return false;
    } 
    else if (/A-Z/.test(password) == true){
        return false;
    }
    else
    {
        return true;
    }
}
