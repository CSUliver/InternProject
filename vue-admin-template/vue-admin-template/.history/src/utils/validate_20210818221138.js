/**
 * Created by PanJiaChen on 16/11/18.
 */

/**
 * @param {string} path
 * @returns {Boolean}
 */
export function isExternal(path) {
  return /^(https?:|mailto:|tel:)/.test(path)
}

/**
 * @param {string} str
 * @returns {Boolean}
 */
export function validUsername(str) {
  const valid_map = ['admin',
                     'whr', 
                     'tempadmin',
                     'testflight',
                     'admin1',
                     'admin2',
                     'admin3',
                     'admin4',
                     'admin5',
                     'admin6',
                     'admin7',
                     'admin8',
                     'admin9',
                    ]
  return valid_map.indexOf(str.trim()) >= 0
}
