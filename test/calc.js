'use strict'
const chai = require('chai')
const expect = chai.expect

function calc (calcString) {
  return Number(calcString)
}

describe('calc', () => {

  it('should return literals as is', () => {
    expect(calc('1')).to.equal(1)
    expect(calc('010')).to.equal(10)
    expect(calc('1.5')).to.equal(1.5)
  })
})

