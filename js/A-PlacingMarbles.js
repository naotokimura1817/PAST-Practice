function main(input) {
  const args = input.split('');
  let cnt = 0;

  for (let i = 0; i < 3; i++) {
    if (args[i] === '1') {
      cnt++;
    }
  }

  console.log(cnt);
}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));