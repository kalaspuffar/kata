'use strict'
const chai = require('chai')
const expect = chai.expect

function calc (calcString) {
  const tokens = calcString.split(' ')
  var lastOperator = '+'
  return tokens.reduce(
    (sum, token) => {
    if (token === '+' || token === '-' || token === '*' ) {
        lastOperator = token
        return sum
      }
      if(lastOperator === '-') {
        return sum - Number(token)
      }
      if(lastOperator === '*') {
        return sum * Number(token)
      }
      return sum + Number(token)
    },
    0
  )
  
}

describe('calc', () => {

  it('should return literals as is', () => {
    expect(calc('1')).to.equal(1)
    expect(calc('1.5')).to.equal(1.5)
  })
  it('should support addition', () => {
    expect(calc('1 + 1')).to.equal(2)
    expect(calc('2 + 1')).to.equal(3)
    expect(calc('2 + 2')).to.equal(4)
    expect(calc('222 + 32')).to.equal(254)
  })
  it('should support subtraction', () => {
    expect(calc('1 - 1')).to.equal(0)
  })
  it('should support multiplication', () => {
    expect(calc('1 * 1')).to.equal(1)
  })
})

