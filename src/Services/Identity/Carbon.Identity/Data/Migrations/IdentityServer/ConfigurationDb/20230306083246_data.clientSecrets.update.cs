using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Carbon.Identity.Data.Migrations.IdentityServer.ConfigurationDb
{
    /// <inheritdoc />
    public partial class dataclientSecretsupdate : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.UpdateData(
                table: "ApiScopes",
                keyColumn: "Id",
                keyValue: 1,
                column: "Created",
                value: new DateTime(2023, 3, 6, 8, 32, 46, 340, DateTimeKind.Utc).AddTicks(2080));

            migrationBuilder.UpdateData(
                table: "ClientSecrets",
                keyColumn: "Id",
                keyValue: 1,
                columns: new[] { "Created", "Value" },
                values: new object[] { new DateTime(2023, 3, 6, 8, 32, 46, 340, DateTimeKind.Utc).AddTicks(2660), "System.Byte[]" });
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.UpdateData(
                table: "ApiScopes",
                keyColumn: "Id",
                keyValue: 1,
                column: "Created",
                value: new DateTime(2023, 3, 6, 8, 10, 7, 441, DateTimeKind.Utc).AddTicks(7000));

            migrationBuilder.UpdateData(
                table: "ClientSecrets",
                keyColumn: "Id",
                keyValue: 1,
                columns: new[] { "Created", "Value" },
                values: new object[] { new DateTime(2023, 3, 6, 8, 10, 7, 441, DateTimeKind.Utc).AddTicks(7580), "carbon@2023" });
        }
    }
}
