#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

// MD5上下文结构
typedef struct {
    uint32_t state[4];    // 状态 (ABCD)
    uint32_t count[2];    // 位数计数器，模2^64 (低32位在前)
    uint8_t buffer[64];   // 输入缓冲区
} MD5_CTX;

// 基本MD5操作
#define F(x, y, z) (((x) & (y)) | ((~x) & (z)))
#define G(x, y, z) (((x) & (z)) | ((y) & (~z)))
#define H(x, y, z) ((x) ^ (y) ^ (z))
#define I(x, y, z) ((y) ^ ((x) | (~z)))

// 循环左移
#define ROTATE_LEFT(x, n) (((x) << (n)) | ((x) >> (32-(n))))

// 四轮操作
#define FF(a, b, c, d, x, s, ac) { \
    (a) += F((b), (c), (d)) + (x) + (uint32_t)(ac); \
    (a) = ROTATE_LEFT((a), (s)); \
    (a) += (b); \
}
#define GG(a, b, c, d, x, s, ac) { \
    (a) += G((b), (c), (d)) + (x) + (uint32_t)(ac); \
    (a) = ROTATE_LEFT((a), (s)); \
    (a) += (b); \
}
#define HH(a, b, c, d, x, s, ac) { \
    (a) += H((b), (c), (d)) + (x) + (uint32_t)(ac); \
    (a) = ROTATE_LEFT((a), (s)); \
    (a) += (b); \
}
#define II(a, b, c, d, x, s, ac) { \
    (a) += I((b), (c), (d)) + (x) + (uint32_t)(ac); \
    (a) = ROTATE_LEFT((a), (s)); \
    (a) += (b); \
}

// 字节顺序转换
static void byte_reverse(uint8_t *buf, unsigned longs) {
    uint32_t t;
    do {
        t = (uint32_t)((uint32_t)buf[3] << 8 | buf[2]) << 16 |
            ((uint32_t)buf[1] << 8 | buf[0]);
        *(uint32_t *)buf = t;
        buf += 4;
    } while (--longs);
}

// MD5初始化
static void MD5_Init(MD5_CTX *ctx) {
    ctx->state[0] = 0x67452301;
    ctx->state[1] = 0xefcdab89;
    ctx->state[2] = 0x98badcfe;
    ctx->state[3] = 0x10325476;
    
    ctx->count[0] = ctx->count[1] = 0;
}

// MD5块处理
static void MD5_Transform(uint32_t state[4], const uint8_t block[64]) {
    uint32_t a = state[0], b = state[1], c = state[2], d = state[3], x[16];
    
    // 将字节块转换为32位整数数组
    for (int i = 0, j = 0; j < 64; i++, j += 4) {
        x[i] = ((uint32_t)block[j]) | (((uint32_t)block[j+1]) << 8) |
               (((uint32_t)block[j+2]) << 16) | (((uint32_t)block[j+3]) << 24);
    }
    
    // 第一轮
    FF(a, b, c, d, x[ 0],  7, 0xd76aa478);
    FF(d, a, b, c, x[ 1], 12, 0xe8c7b756);
    FF(c, d, a, b, x[ 2], 17, 0x242070db);
    FF(b, c, d, a, x[ 3], 22, 0xc1bdceee);
    FF(a, b, c, d, x[ 4],  7, 0xf57c0faf);
    FF(d, a, b, c, x[ 5], 12, 0x4787c62a);
    FF(c, d, a, b, x[ 6], 17, 0xa8304613);
    FF(b, c, d, a, x[ 7], 22, 0xfd469501);
    FF(a, b, c, d, x[ 8],  7, 0x698098d8);
    FF(d, a, b, c, x[ 9], 12, 0x8b44f7af);
    FF(c, d, a, b, x[10], 17, 0xffff5bb1);
    FF(b, c, d, a, x[11], 22, 0x895cd7be);
    FF(a, b, c, d, x[12],  7, 0x6b901122);
    FF(d, a, b, c, x[13], 12, 0xfd987193);
    FF(c, d, a, b, x[14], 17, 0xa679438e);
    FF(b, c, d, a, x[15], 22, 0x49b40821);
    
    // 第二轮
    GG(a, b, c, d, x[ 1],  5, 0xf61e2562);
    GG(d, a, b, c, x[ 6],  9, 0xc040b340);
    GG(c, d, a, b, x[11], 14, 0x265e5a51);
    GG(b, c, d, a, x[ 0], 20, 0xe9b6c7aa);
    GG(a, b, c, d, x[ 5],  5, 0xd62f105d);
    GG(d, a, b, c, x[10],  9, 0x02441453);
    GG(c, d, a, b, x[15], 14, 0xd8a1e681);
    GG(b, c, d, a, x[ 4], 20, 0xe7d3fbc8);
    GG(a, b, c, d, x[ 9],  5, 0x21e1cde6);
    GG(d, a, b, c, x[14],  9, 0xc33707d6);
    GG(c, d, a, b, x[ 3], 14, 0xf4d50d87);
    GG(b, c, d, a, x[ 8], 20, 0x455a14ed);
    GG(a, b, c, d, x[13],  5, 0xa9e3e905);
    GG(d, a, b, c, x[ 2],  9, 0xfcefa3f8);
    GG(c, d, a, b, x[ 7], 14, 0x676f02d9);
    GG(b, c, d, a, x[12], 20, 0x8d2a4c8a);
    
    // 第三轮
    HH(a, b, c, d, x[ 5],  4, 0xfffa3942);
    HH(d, a, b, c, x[ 8], 11, 0x8771f681);
    HH(c, d, a, b, x[11], 16, 0x6d9d6122);
    HH(b, c, d, a, x[14], 23, 0xfde5380c);
    HH(a, b, c, d, x[ 1],  4, 0xa4beea44);
    HH(d, a, b, c, x[ 4], 11, 0x4bdecfa9);
    HH(c, d, a, b, x[ 7], 16, 0xf6bb4b60);
    HH(b, c, d, a, x[10], 23, 0xbebfbc70);
    HH(a, b, c, d, x[13],  4, 0x289b7ec6);
    HH(d, a, b, c, x[ 0], 11, 0xeaa127fa);
    HH(c, d, a, b, x[ 3], 16, 0xd4ef3085);
    HH(b, c, d, a, x[ 6], 23, 0x04881d05);
    HH(a, b, c, d, x[ 9],  4, 0xd9d4d039);
    HH(d, a, b, c, x[12], 11, 0xe6db99e5);
    HH(c, d, a, b, x[15], 16, 0x1fa27cf8);
    HH(b, c, d, a, x[ 2], 23, 0xc4ac5665);
    
    // 第四轮
    II(a, b, c, d, x[ 0],  6, 0xf4292244);
    II(d, a, b, c, x[ 7], 10, 0x432aff97);
    II(c, d, a, b, x[14], 15, 0xab9423a7);
    II(b, c, d, a, x[ 5], 21, 0xfc93a039);
    II(a, b, c, d, x[12],  6, 0x655b59c3);
    II(d, a, b, c, x[ 3], 10, 0x8f0ccc92);
    II(c, d, a, b, x[10], 15, 0xffeff47d);
    II(b, c, d, a, x[ 1], 21, 0x85845dd1);
    II(a, b, c, d, x[ 8],  6, 0x6fa87e4f);
    II(d, a, b, c, x[15], 10, 0xfe2ce6e0);
    II(c, d, a, b, x[ 6], 15, 0xa3014314);
    II(b, c, d, a, x[13], 21, 0x4e0811a1);
    II(a, b, c, d, x[ 4],  6, 0xf7537e82);
    II(d, a, b, c, x[11], 10, 0xbd3af235);
    II(c, d, a, b, x[ 2], 15, 0x2ad7d2bb);
    II(b, c, d, a, x[ 9], 21, 0xeb86d391);
    
    state[0] += a;
    state[1] += b;
    state[2] += c;
    state[3] += d;
}

// MD5更新
static void MD5_Update(MD5_CTX *ctx, const uint8_t *input, size_t input_len) {
    uint32_t i, index, part_len;
    
    // 计算当前缓冲区中的字节数
    index = (uint32_t)((ctx->count[0] >> 3) & 0x3F);
    
    // 更新位数计数器
    if ((ctx->count[0] += ((uint32_t)input_len << 3)) < ((uint32_t)input_len << 3)) {
        ctx->count[1]++;
    }
    ctx->count[1] += ((uint32_t)input_len >> 29);
    
    part_len = 64 - index;
    
    // 处理尽可能多的完整块
    if (input_len >= part_len) {
        memcpy(&ctx->buffer[index], input, part_len);
        byte_reverse(ctx->buffer, 16);
        MD5_Transform(ctx->state, ctx->buffer);
        
        for (i = part_len; i + 63 < input_len; i += 64) {
            MD5_Transform(ctx->state, &input[i]);
        }
        
        index = 0;
    } else {
        i = 0;
    }
    
    // 保存剩余输入
    memcpy(&ctx->buffer[index], &input[i], input_len - i);
}

// MD5结束，生成最终哈希值
static void MD5_Final(uint8_t digest[16], MD5_CTX *ctx) {
    uint8_t bits[8];
    uint32_t index, pad_len;
    
    // 保存位数
    for (int i = 0; i < 8; i++) {
        bits[i] = (uint8_t)(ctx->count[i >> 2] >> ((i & 3) << 3));
    }
    
    // 填充到56字节（448位）
    index = (uint32_t)((ctx->count[0] >> 3) & 0x3f);
    pad_len = (index < 56) ? (56 - index) : (120 - index);
    MD5_Update(ctx, (uint8_t*)"\x80", 1);
    while (pad_len-- > 1) {
        MD5_Update(ctx, (uint8_t*)"\0", 1);
    }
    
    // 附加长度（低字节在前）
    MD5_Update(ctx, bits, 8);
    
    // 存储状态到摘要
    for (int i = 0; i < 4; i++) {
        digest[i*4+0] = (uint8_t)(ctx->state[i] & 0xff);
        digest[i*4+1] = (uint8_t)((ctx->state[i] >> 8) & 0xff);
        digest[i*4+2] = (uint8_t)((ctx->state[i] >> 16) & 0xff);
        digest[i*4+3] = (uint8_t)((ctx->state[i] >> 24) & 0xff);
    }
    
    // 清除敏感信息
    memset(ctx, 0, sizeof(*ctx));
}

// 计算字符串的MD5哈希值
void calculate_string_md5(const char *string, uint8_t *md5_hash) {
    MD5_CTX context;
    MD5_Init(&context);
    MD5_Update(&context, (const uint8_t *)string, strlen(string));
    MD5_Final(md5_hash, &context);
}

// 计算文件的MD5哈希值
int calculate_file_md5(const char *filename, uint8_t *md5_hash) {
    FILE *file = fopen(filename, "rb");
    if (!file) {
        return -1; // 文件打开失败
    }

    MD5_CTX context;
    MD5_Init(&context);

    uint8_t buffer[1024];
    size_t bytes_read;
    while ((bytes_read = fread(buffer, 1, sizeof(buffer), file)) != 0) {
        MD5_Update(&context, buffer, bytes_read);
    }

    MD5_Final(md5_hash, &context);
    fclose(file);
    return 0;
}

// 将MD5哈希值转换为十六进制字符串
void md5_to_hex(const uint8_t *md5_hash, char *hex_output) {
    for (int i = 0; i < 16; i++) {
        sprintf(hex_output + (i * 2), "%02x", md5_hash[i]);
    }
    hex_output[32] = '\0';
}

// 比较两个MD5哈希值是否相同
int compare_md5(const uint8_t *hash1, const uint8_t *hash2) {
    return memcmp(hash1, hash2, 16) == 0;
}

// 打印帮助信息
void print_help() {
    printf("MD5验证程序使用方法:\n");
    printf("  -s <字符串>       计算字符串的MD5哈希值\n");
    printf("  -f <文件路径>     计算文件的MD5哈希值\n");
    printf("  -c <哈希值>       验证哈希值（与-s或-f一起使用）\n");
    printf("  -h               显示帮助信息\n");
    printf("\n示例:\n");
    printf("  md5_check -s \"hello world\"\n");
    printf("  md5_check -f test.txt -c 5eb63bbbe01eeed093cb22bb8f5acdc3\n");
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        print_help();
        return 1;
    }

    int mode = 0; // 0: none, 1: string, 2: file
    char *input = NULL;
    char *hash_to_check = NULL;

    // 解析命令行参数
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-s") == 0 && i + 1 < argc) {
            mode = 1;
            input = argv[++i];
        } else if (strcmp(argv[i], "-f") == 0 && i + 1 < argc) {
            mode = 2;
            input = argv[++i];
        } else if (strcmp(argv[i], "-c") == 0 && i + 1 < argc) {
            hash_to_check = argv[++i];
        } else if (strcmp(argv[i], "-h") == 0) {
            print_help();
            return 0;
        }
    }

    if (mode == 0) {
        printf("错误: 未指定输入模式(-s或-f)\n");
        print_help();
        return 1;
    }

    uint8_t md5_hash[16];
    char hex_hash[33];

    if (mode == 1) {
        // 字符串模式
        calculate_string_md5(input, md5_hash);
        md5_to_hex(md5_hash, hex_hash);
        printf("字符串 \"%s\" 的MD5哈希值: %s\n", input, hex_hash);
    } else if (mode == 2) {
        // 文件模式
        if (calculate_file_md5(input, md5_hash) != 0) {
            printf("错误: 无法打开文件 %s\n", input);
            return 1;
        }
        md5_to_hex(md5_hash, hex_hash);
        printf("文件 %s 的MD5哈希值: %s\n", input, hex_hash);
    }

    // 验证哈希值
    if (hash_to_check != NULL) {
        if (strlen(hash_to_check) != 32) {
            printf("错误: 提供的MD5哈希值长度不正确\n");
            return 1;
        }

        printf("验证结果: ");
        if (strcasecmp(hex_hash, hash_to_check) == 0) {
            printf("匹配成功\n");
        } else {
            printf("匹配失败\n");
            printf("期望: %s\n", hash_to_check);
            printf("实际: %s\n", hex_hash);
            return 1;
        }
    }

    return 0;
}