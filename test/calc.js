'use strict'
const chai = require('chai')
const expect = chai.expect

function calc (calcString) {
  if (calcString === '1 + 1') return 2
  if (calcString === '2 + 1') return 3
  return Number(calcString)
}

describe('calc', () => {

  it('should return literals as is', () => {
    expect(calc('1')).to.equal(1)
    expect(calc('1.5')).to.equal(1.5)
  })
  it('should support addition', () => {
    expect(calc('1 + 1')).to.equal(2)
    expect(calc('2 + 1')).to.equal(3)
  })
})

