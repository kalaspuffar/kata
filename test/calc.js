'use strict'
const chai = require('chai')
const expect = chai.expect


const operators = '+-*/'.split('')
const term_ops = '+-'.split('')
const prod_ops = '*/'.split('')

function calc (calcString) {
  const tokens = calcString.split(' ')
  var values = []
  for (let i = 0; i < tokens.length; i++) {
    if (operators.indexOf(tokens[i]) === -1) {
      values.push(Number(tokens[i]))
    } else {
      values.push(tokens[i])
    }
  }

  var result = []
  for (let i = 0; i < values.length; i++) {
    if (values[i] === '*' ) {
      let leftSide = result.pop()
      result.push(leftSide * values[++i])
    } else if (values[i] === '/') {
      let leftSide = result.pop()
      result.push(leftSide / values[++i])
    } else {
      result.push(values[i])
    }
  }
  values = result

  result = []
  for (let i = 0; i < values.length; i++) {
    if (values[i] === '+' ) {
      let leftSide = result.pop()
      result.push(leftSide + values[++i])
    } else if (values[i] === '-') {
      let leftSide = result.pop();
      result.push(leftSide - values[++i])
    } else {
      result.push(values[i])
    }
  }
  return result[0]
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
  it('should support division', () => {
    expect(calc('2 / 1')).to.equal(2)
  })
  it('should handle addition and division', () => {
    expect(calc('1 + 2 * 3')).to.equal(7)
  })
})

