function solution(price, money, count) {
  let currentPrice = price;
  let totalPrice = 0;
  for (let i = 1; i <= count; i++) {
    totalPrice += currentPrice;
    currentPrice += price;
  }

  if (money >= totalPrice) return 0;
  else {
    return totalPrice - money;
  }
}
