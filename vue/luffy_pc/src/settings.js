export default{
    Host:'http://api.luffycity.cn:8000',
    token(){
      return localStorage.token || sessionStorage.token;
    }
}
