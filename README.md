# skvn-ldms-api


# Login test example
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"uid":"admin","password":"test1234"}' \
  https://ol20kocmsg.execute-api.ap-northeast-2.amazonaws.com/dev/common/login/